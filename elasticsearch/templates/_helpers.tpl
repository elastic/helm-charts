{{/* vim: set filetype=mustache: */}}
{{/*
Expand the name of the chart.
*/}}
{{- define "name" -}}
{{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{/*
Create a default fully qualified app name.
We truncate at 63 chars because some Kubernetes name fields are limited to this (by the DNS naming spec).
*/}}
{{- define "fullname" -}}
{{- $name := default .Chart.Name .Values.nameOverride -}}
{{- printf "%s-%s" .Release.Name $name | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{- define "uname" -}}
{{ .Values.clusterName }}-{{ .Values.nodeGroup }}
{{- end -}}

{{- define "masterService" -}}
{{- if empty .Values.masterService -}}
{{ .Values.clusterName }}-master
{{- else -}}
{{ .Values.masterService }}
{{- end -}}
{{- end -}}

{{- define "endpoints" -}}
{{- $replicas := .replicas | int }}
{{- $uname := printf "%s-%s" .clusterName .nodeGroup }}
  {{- range $i, $e := untilStep 0 $replicas 1 -}}
{{ $uname }}-{{ $i }},
  {{- end -}}
{{- end -}}

{{- define "esMajorVersion" -}}
{{- if .Values.esMajorVersion -}}
{{ .Values.esMajorVersion }}
{{- else -}}
{{- $version := int (index (.Values.imageTag | splitList ".") 0) -}}
  {{- if and (contains "docker.elastic.co/elasticsearch/elasticsearch" .Values.image) (not (eq $version 0)) -}}
{{ $version }}
  {{- else -}}
7
  {{- end -}}
{{- end -}}
{{- end -}}
